import React, { useEffect, useState} from "react";
import makeGETRequest from "../../../http_requests/getRequest";
import HomePageTemplate from "../../templates/HomePageTemplate/HomePageTemplate";
import "./HomePage.css";
import url from "../../../url";
import { ToastContainer, toast } from "react-toastify";

function HomePage() {
    const [notificationId,setNotificationId]=useState('');
    
    useEffect(()=>{
        const interval=setInterval(async ()=>{
            try{
                var response = await makeGETRequest(url + "calling-status");
                console.log(response.data);
                if(response.data.id!==notificationId){
                    setNotificationId(_=>response.data.id.toString());
                    if(response.data.type==="warning"){
                        toast.warn(response.data.message,{
                            position: toast.POSITION.TOP_RIGHT,
                        });
                    }
                    if(response.data.type==="error"){
                        toast.error(response.data.message,{
                            position: toast.POSITION.TOP_RIGHT,
                        });
                    }
                    if(response.data.type==="success"){
                        toast.success(response.data.message,{
                            position: toast.POSITION.TOP_RIGHT,
                        });
                    }
                    if(response.data.type==="info"){
                        toast.info(response.data.message,{
                            position: toast.POSITION.TOP_RIGHT,
                        });
                    }
                }
            }catch(e){
                toast.error("An error occued in fetching status");
            }
        },1000);
        return ()=>clearInterval(interval);
    },[notificationId]);

    return (
        <div className="home-page">
            <ToastContainer/>
            <HomePageTemplate/>
        </div>
    );
}

export default HomePage;