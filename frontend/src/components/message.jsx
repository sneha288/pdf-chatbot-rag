function Message({sender,text}){
    return(
        <div className={
            sender=="user"? "message user-message":"message ai-message"
    }>
        <p>{text}</p>
    </div>
    );
}

export default Message;