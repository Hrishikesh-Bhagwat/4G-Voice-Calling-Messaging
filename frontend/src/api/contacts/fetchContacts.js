import {url} from "../../url"
import makeGetRequest from "../../http_requests/getRequest";

export default async function fetchContacts(){
    try{
        var response = await makeGetRequest(url+"contacts");
        var contacts=[];
        for(var i=0;i<response.data.length;i++){
            contacts.push(
                {
                    id: response.data[i]["id"],
                    name: response.data[i]["name"],
                    phone: response.data[i]["phone"],
                    isSelected: response.data[i]["selected"]
                }
            );
        }
        return contacts;
    }catch(e){
        console.log(e);
        return [];
    }
}