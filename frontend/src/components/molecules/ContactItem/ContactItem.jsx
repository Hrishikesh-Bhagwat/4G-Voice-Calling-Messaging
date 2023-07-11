// import DeleteIcon from '@mui/icons-material/Delete';
// import ListItem from '@mui/material/ListItem';
// import ListItemText from '@mui/material/ListItemText';
// import { IconButton } from '@mui/material';
import { useState } from "react";
import "./ContactItem.css";
import { FaTrashAlt } from 'react-icons/fa';
import url from "../../../url";
import {toast} from "react-toastify";


function ContactItem({ id, name, phone, isSelected, reload}) {
    const [isChecked, setIsChecked] = useState(isSelected);

    async function updateContactStatus(event) {
        setIsChecked(event.target.checked);
        console.log(event.target.checked);
        fetch(`${url}contacts/update-status`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'id': id, 'status': !isChecked })
        })
            .then(response => {
                if(response.status!==200){
                    toast.error("Failed to update contact list");
                }
                return response.json();
            })
            .then(async responseData => {
                await reload();
                console.log(responseData);
            })
            .catch(error => {
                // Handle any errors that occurred during the request
                toast.error("Failed to add contact to list");
                console.error(error);
            });
    }
    async function removeContact() {
        fetch(`${url}contacts/delete-contact`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'id': id})
        })
            .then(response => response.json())
            .then(async responseData => {
                await reload();
                console.log(responseData);
            })
            .catch(error => {
                // Handle any errors that occurred during the request
                toast.error("Failed to delete contact!");
                console.error(error);
            });
    }

    return (
        <div className="contact-item">
            <div className='checkbox-space'>
                <input type='checkbox' className='checkbox' onChange={(event) => { updateContactStatus(event) }} checked={isChecked} />
            </div>
            <div className='checkbox-tile-number'>
                <div>
                    <b>{name}</b>
                </div>
                <div>{phone}</div>
            </div>
            <div className='checkbox-delete'>
                <div onClick={removeContact}><FaTrashAlt style={{ color: "red" }} /></div>
            </div>
        </div>
    );
}

export default ContactItem;