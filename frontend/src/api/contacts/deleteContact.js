import makePOSTRequest from "../../http_requests/postRequest";
import {url} from "../../url"

export default async function deleteContact(id){
    var url=url + "contacts" + "/delete-contact";
    try{
        var response= await makePOSTRequest(url,{id: id});
        return response;
    }
    catch(e){
        print(e);
        return null;
    }
}