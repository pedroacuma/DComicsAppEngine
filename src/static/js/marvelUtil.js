/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 * @author Pedro Ávila
 */

function foo(callback){
    
    var autor = "";
    autor += document.getElementById("autor").value;
    var firstName = autor.substr(0,autor.indexOf(" "));
    var lastName = autor.substr(autor.indexOf(" ")+1, autor.length-1);
      
    console.log(firstName);
    console.log(lastName);
        
    var url = "http://gateway.marvel.com/v1/public/creators?firstName=" + firstName +"&lastName=" + lastName + "&ts=1&apikey=b25a37a62f6e92fa1467788ac668064e&hash=5f69eb74d0221852f735494c961b5d3e";      
    var idAutor;
    
    $.ajax({
        url: url,
        type: "GET",
           
        success: function(data){
            callback(data.data.results[0].id);                
        }
    });
}



function comicsByAuthor(result) {
        
        var idAutor = result;
        
        var url = "http://gateway.marvel.com/v1/public/comics?creators="+ idAutor.toString() +"&orderBy=-onsaleDate&ts=1&apikey=b25a37a62f6e92fa1467788ac668064e&hash=5f69eb74d0221852f735494c961b5d3e";
        console.log(url);
        var marvelContainer = document.getElementById("marvel");
        var message = document.getElementById("message");
        
        $.ajax({
            url: url,
            type: "GET",
            
            beforeSend: function(){
                message.innerHTML = "Cargando...";
            },
            
            complete: function(){
                message.innerHTML = "Cargado correctamente";
            },
            error: function(){
                message.innerHTML = "Problema cargando la api";
            },
            success: function(data){

               var string = "";
               string += data.attributionHTML;
               string += "<div class='row'>";
               
                for(var i=0; i<data.data.results.length; i++){
                   var element = data.data.results[i];
                   console.log(element.title);
                   
                    string += "<div class='col-md-3'>";
                    string += "<a href='" + element.urls[0].url + "' target='_blank'>"
                    string += "<img src='" + element.thumbnail.path + "/portrait_fantastic." +
                        element.thumbnail.extension  + "' />";
                    string += "</a>";
                    string += "<h3>" + element.title + "</h3>";
                    string += "</div>";
                    
                    if((i+1)%4 == 0){
                        string += "</div>";
                        string += "<div class='row'>";
                    }
               }
               marvelContainer.innerHTML = string;
            }
          });
};


foo(comicsByAuthor);



