function Gravador(params) {
    
}


Gravador.prototype.JlinkWrite = function (device, caminho, callBack, reles = 0, speed = 2000) {
    SetEstado("################### Gravando Firmware ###################")


    /// ex: Gravador.JlinkWrite("atsamd09d14a","2000", RastAPI.getCookie("Firmware"))

    Teste.DesligaReles(()=>{
        Teste.LigaReles(reles,()=>{
            setTimeout(() => { 
                caminho = caminho.replace(/([\\])/g, "\/")                        
                var csvComandos =
                "'device  "+ device +"';" +
                "'speed " + speed +"';" +
                "'if swd';" + 
                "'connect';" +   
               // "'erase';" + 
                "'loadfile \"" + caminho + "\"';" +
                "'loadfile \"" + caminho + "\"';" +
                "'rx 300';" +
                "'g';" +
                "'IsHalted';"+
                "'exit'";
        
                pvi.runInstructionS("segger.jlink.runCommandList", ["\"" + csvComandos + "\""], function (csvRetorno) {        
                    csvRetorno = csvRetorno
                        ok = false
                    if (csvRetorno.includes("Contents already match")) {
                        ok = true
                    } else {
                        ok = false
                        Falhas.set("Gravação", "Não foi possivel fazer a gravação do controlador") 
                        Falhas.set("LogGravador", csvRetorno)
                        //console.log ("Gravação =>",csvRetorno);               
                    }               
                    callBack(ok, csvRetorno)       
                })
        }, 800)
        })
        
    })
}

