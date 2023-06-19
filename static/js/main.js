async function getFileType(){
    try{
        const [fileHandle] = await window.showOpenFilePicker();

        const[filedata] = await fileHandle.getFile();

        console.log(filedata)
    }catch(error){
        console.log(`Your error is ${error}`)
    }

}