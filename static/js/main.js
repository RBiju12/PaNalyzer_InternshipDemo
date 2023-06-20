async function getFileType(){
    try{
        const [fileGrab] = await window.showOpenFilePicker();

        const filecontent = await fileGrab.getFile();

        const filetype = filecontent.name.split(".").pop();

        //filetype access .name from the console

        if(filetype !== "exe" || filetype === null){
            alert("Filetype must be .exe");
        }
    }
    catch(error){
        console.log(`Your error is: ${error}`)
    }



}