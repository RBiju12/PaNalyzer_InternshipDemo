async function getFileType(){
    try{
        const [fileGrab] = await window.showOpenFilePicker();

        const filecontent = await fileGrab.getFile();

        //const versionumber = filecontent.

        //takes filecontent in console then grabs the file extension name

        const filetype = filecontent.name.split(".").pop();
        
        const [testfile, ...resttestfile] = filecontent.name.split("-");

        //splits the file name to test out application
        const present = 2023

        const url = "\nhttps://www.anaconda.com/download"

        //filetype access .name from the console

        //Only accepts .exe files
        if(filetype === "exe"){
            if(resttestfile[0] < present){
                alert("You need to download the Latest version of Ananaconda: ".concat(url));
            }
            else{

                alert("You already meet the latest version requirements");
            }
        }

        else if(filetype !== "exe" || filetype === null){
            alert("Filetype must be .exe");
            console.log(filecontent)
        }

        else{
            alert('File is not compatible')
        }

    }
    catch(error){
        console.log(`Your error is: ${error}`)
    }



}