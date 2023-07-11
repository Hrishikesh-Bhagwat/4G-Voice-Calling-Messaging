import { useEffect, useState } from "react";
import CallSectionTitle from "../../atoms/CallSectionTitle/CallSectionTitle";
import CallAddSection from "../CallAddSection/CallAddSection";
import ContactList from "../ContactList/ContactList";
import "./CallSection.css";
import url from "../../../url";
import makeGETRequest from "../../../http_requests/getRequest";

function CallSection(props) {
    const [contactList, setContactList] = useState([]);
    async function getContacts() {
        try {
            var response = await makeGETRequest(url + "contacts");
            var temp = [];
            for (var i = 0; i < response.data.length; i++) {
                temp.push(
                    {
                        id: response.data[i].id,
                        name: response.data[i].name,
                        phone: response.data[i].phone,
                        isSelected: response.data[i].selected,
                    }
                );
            }
            setContactList(temp);
        } catch (e) {
            console.log(e);
            setContactList([]);
        }
    }
    useEffect(
        () => {
            getContacts();
        },
        []
    );
    return (
        <div className="call-section">
            <CallSectionTitle />
            <ContactList contactList={contactList} reload={getContacts}/>
            <CallAddSection reload={getContacts} disabled={props.disabled}/>
        </div>
    );
}

export default CallSection;