import axios from "axios";

function makeGETRequest(url){
    return axios.get(url);
}

export default makeGETRequest;