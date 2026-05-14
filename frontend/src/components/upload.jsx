import { useState } from "react";
import axios from "axios";

function Upload({setpdfUploaded}){
    const [file, setFile] = useState(null);
    const [loading, setLoading]=useState(false);
    const [message, setMessage]=useState("");

    const handleUpload=async()=>{
        if(!file){
            alert("Please selct a PDF file");
            return;
        }
        try{
            setLoading(true);
            const formData=new FormData();
            formData.append("file",file);

            const response =await axios.post(
                "http://localhost:5000/upload",formData,
                {
                    headers:{
                        "Content-Type":"multipart/form-data"
                    }
                }
            );

            setMessage(response.data.message);
            setpdfUploaded(true);
        }
        catch(error){
            console.log(error);
            setMessage(error.response?.data?.error || "Upload failed");
        }
    };

    return(
        <div className="card">
            <h2>Upload PDF</h2>
            <input type="file"
              accept="application/pdf"
              onChange={(e)=>setFile(e.target.files[0])}/>

            <button onClick={handleUpload} disabled={loading}>{loading?"uploading...":"Upload"}</button>

            {message && <p>{message}</p>}
        </div>
    );
}

export default Upload