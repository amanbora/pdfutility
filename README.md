# pdfutility

I have made two python scripts:
    - nlp.py uses nlp modules (complete/fixed)
    - libre.py uses LibreOffice to convert pdfs, it requires LibreOffice to be installed in the system (customizable/under development)

Installing Dependencies:
    python (libre_env) : pip install -r requirementsLibre.txt
    python (nlp_env) : pip install -r requirementsLibre.txt
    node : cd node-server -> npm install
    angular : cd node-server/public/client -> npm install

Start Node-Server (server):
    cd node-server -> npm run gulp
    - runs at localhost:8080
    - consists of routes to interact with python scripts

Start Angular-Server (client):
    cd node-server/public/client -> ng serve
    - runs at localhost:4200
    - used to upload pdf/docx and show output as JSON


Things To Do:
    - Work on frontend(styling)
    - Better management of code
    - Adding database configurations