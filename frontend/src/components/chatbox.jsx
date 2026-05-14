import { useState } from "react";
import axios from "axios";
import Message from "./message";

function Chatbox({pdfUploaded}){
    const [question, setQuestion] = useState("");
    const [message, setMessage]=useState([]);
    const [loading, setLoading]=useState(false);

    const handleAsk=async()=>{
        if(!question.trim()){
            return;
        }

        const userMessage={
            sender:"User",
            text:question
        };

        setMessage((prev)=>[
            ...prev,
            userMessage
        ]);

        try{
            setLoading(true);

            const response=await axios.post(
                "http://localhost:5000/ask",
                {question:question}
            );

            const aiMessage={sender:"ai", text:response.data.answer};

            setMessage((prev)=>[
                ...prev,aiMessage
            ]);
        }

        catch(error){
            const errorMessage={
                sender:"ai",
                text:error.response?.data?.error || "Something went wrong"
            };

            setMessage((prev)=>[
                ...prev, errorMessage
            ]);
        }
        finally{
            setLoading(false);
            setQuestion("");
        }
    };

    return(
        <div className="card">
            <h2>Ask questions</h2>{
                !pdfUploaded && 
                <p>Please upload a PDF first</p>
            }

            <div className="chat-container">
                {
                    message.map((message, index)=>(
                        <Message 
                         key={index}
                         sender={message.sender}
                         text={message.text}
                         />
                    ))
                }
            </div>
            <div className="input">
                <input 
                type="text"
                placeholder="Ask a question..."
                value={question}
                onChange={(e)=>setQuestion(e.target.value)}
                disabled={!pdfUploaded}/>

                <button onClick={handleAsk}
                disabled={!pdfUploaded || loading}>
                    {loading? "Thinking.....":"Ask"}
                </button>
            </div>
        </div>
        
    );
}

export default Chatbox