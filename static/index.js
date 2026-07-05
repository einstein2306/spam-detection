document.addEventListener("DOMContentLoaded",()=>{


    document.querySelector("#form").onsubmit = () =>{

        const request = new XMLHttpRequest();

        const mesg = document.querySelector("#message").value;
        document.querySelector("#message").value = "";

        document.querySelector("#spam").innerHTML = '<div class="spinner-border spinner-border-sm text-danger"></div>';
        document.querySelector("#ham").innerHTML = '<div class="spinner-border spinner-border-sm text-success"></div>';
        document.querySelector("#pred").innerHTML = '<div class="spinner-border spinner-border-sm text-primary"></div>';

        request.open("POST","/predict");

        request.onload = () =>{

            const data = JSON.parse(request.responseText);

            if(data.success){
                document.querySelector("#spam").innerHTML = data.spam + '%';
                document.querySelector("#ham").innerHTML = data.ham + "%";
                document.querySelector("#pred").innerHTML = data.pred;
                document.querySelector(".clear").disabled = false;
                 
            }else{
                document.querySelector("#spam").innerHTML = 'something';
                document.querySelector("#ham").innerHTML = 'went';
                document.querySelector("#pred").innerHTML = 'wrong';
            }
        };

        const form = new FormData();
        form.append("message",mesg);

        request.send(form);
        return false;
    };

});

function clearData(){
    document.querySelector('#spam').innerHTML = '0%';
    document.querySelector('#ham').innerHTML = '0%';
    document.querySelector('#pred').innerHTML = '----';
    document.querySelector(".clear").disabled = true;
}