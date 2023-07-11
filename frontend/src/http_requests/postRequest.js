import axios from "axios";

function makePOSTRequest(url,body){
    return axios.post(url,body);
}

export default makePOSTRequest;