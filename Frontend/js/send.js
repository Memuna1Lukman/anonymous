const sendBtn = document.getElementById("send");
const textArea = document.getElementById("text_area");
// store data with setItem
const username = "muna"
async function sendMessage(){
    try {
        const response =  await fetch(`http://127.0.0.1:8000/sendermsg/${username}`,
            {
                method: "POST",
                headers:{
                    "content-Type" : "application/json"
                },
                body: JSON.stringify({
                    content: textArea.value
                })
            }
        );
        const data = await response.json()
        console.log(data);
        textArea.value = "";
        alert("Message sent successfully");
        // textArea.value = "Thanks for sending your anonymous message";
    } catch (error) {
        console.error("Error fetching data: ", error);
    }
}
sendBtn.addEventListener("click",(e)=>{
    e.preventDefault();
    
    sendMessage();
    return textArea;
});





// retrieve data with getItem
// function getToken() {
//     const savedToken = localStorage.getItem('token');
//     if (savedToken){
//         const saved = JSON.parse(savedToken);
//         console.log("Retrieved from storage: ", saved.username);
//         return saved;
//     }else{
//         console.log("No data found in localStorage");
//         return null;
//     }
// }




