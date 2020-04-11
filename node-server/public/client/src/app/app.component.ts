import { Component, OnInit, ElementRef, Input} from '@angular/core';
import { FileUploader } from 'ng2-file-upload';
import { Http, Response } from '@angular/http';
import { map } from 'rxjs/operators';
import { Observable, of, Subject } from 'rxjs';

const URL = 'http://localhost:8080/uploadPdf';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'client';
  output = null;

  public uploader: FileUploader = new FileUploader({url: 'http://localhost:8080/uploadPdf'});

  ngOnInit(){
    //override the onAfterAddingfile property of the uploader so it doesn't authenticate with //credentials.
    this.uploader.onAfterAddingFile = (file)=> { file.withCredentials = false; };
    //overide the onCompleteItem property of the uploader so we are
    //able to deal with the server response.
    // this.uploader.onCompleteItem = (item: any, response: any, status: any, headers: any) => {
    //   console.log('PdfUpload:uploaded:', item, status, response);
    // };
  }

  constructor(private http: Http, private el: ElementRef){}

  getOutput(){
    console.log("called");
    this.http.get('http://localhost:8080/pdfOutput').subscribe(data=>{
      console.log(data.text());
      alert(data);
      this.output = JSON.parse(JSON.stringify(data.text()));
    })
  }


  upload(){
    let inputEl : HTMLInputElement = this.el.nativeElement.querySelector('#file');
    let formData = new FormData();
    formData.append('file', inputEl.files.item(0));
    this.http.post(URL, formData).pipe(
      map((res)=>this.output))
      .subscribe(
          (success) => {
              // alert(success);
              console.log(`yesss`)
              this.getOutput();
      },
      (error) => alert(error)
    )
  }



}
