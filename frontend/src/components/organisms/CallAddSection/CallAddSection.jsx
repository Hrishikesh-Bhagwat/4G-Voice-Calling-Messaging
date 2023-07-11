import "./CallAddSection.css";
import { FaAddressBook, FaPhone } from "react-icons/fa";
import url from "../../../url";
import { Modal, Box, TextField, Button } from "@mui/material";
import { useState } from "react";
import axios from "axios";
import {toast} from "react-toastify";

const CustomButton = (props) => {
    return (
        <button
            style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                backgroundColor: props.color,
                color: 'white',
                width: "80%",
                border: 'none',
                paddingTop: "9px",
                paddingBottom: "9px",
                marginTop: props.mt,
                borderRadius: '5px',
                cursor: 'pointer',
            }}
            onClick={props.click}
            disabled={props.disabled}
        >
            {props.type === "phone" ? <FaPhone style={{ marginRight: '5px' }} /> : <FaAddressBook style={{ marginRight: '5px' }} />}
            {props.type === "phone" ? "MAKE CALL" : "NEW CONTACT"}
        </button>
    );
};

function CallAddSection(props) {
    function isStringValid(phoneNumber) {
        return /^\d{10}$/.test(phoneNumber);
    }
    async function addContact() {
        if (name.trim() === '') {
            console.log(name);
            setError('Please enter valid name');
            return;
        }
        if (!isStringValid(phone)) {
            setError('Please enter valid phone number');
            return;
        }
        fetch(`${url}contacts/add-contact`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: name, phone: phone })
        })
            .then(response => response.json())
            .then(async responseData => {
                await props.reload();
                console.log(responseData);
                setOpenModal(false);
                setName('');
                setPhone('');
                setError('');
            })
            .catch(error => {
                // Handle any errors that occurred during the request
                setError("Failed to add new contact!");
                console.error(error);
            }).finally(() => {
                
            });
    }
    const [openModal, setOpenModal] = useState(false);
    const [phone, setPhone] = useState('');
    const [name, setName] = useState('');
    const [error, setError] = useState('');
    return (
        <div className="call-add-section">
            <Modal open={openModal} onClose={() => {
                setOpenModal(false);
                setPhone('');
                setName('');
                setError('');
            }} style={{ padding: "0px" }}>
                <Box
                    sx={{
                        position: 'absolute',
                        top: '50%',
                        left: '50%',
                        transform: 'translate(-50%, -50%)',
                        width: 380,
                        height: 250,
                        bgcolor: 'background.paper',
                        outline: 'none',
                        boxShadow: 24,
                        p: 2,
                    }}
                >
                    <div>
                        <b style={{ fontSize: "18px" }}>Add New Contact</b>
                    </div>
                    <TextField
                        label="Name"
                        variant="outlined"
                        fullWidth
                        margin="normal"
                        value={name}
                        onChange={e => setName(e.target.value)}
                    />
                    <TextField
                        label="Phone"
                        variant="outlined"
                        fullWidth
                        margin="normal"
                        value={phone}
                        onChange={e => setPhone(e.target.value)}
                    />
                    <div style={{ width: "100%", display: "flex", justifyContent: "center", marginTop: "3px", marginBottom: "3px",color:"red"}}>
                        {error}
                    </div>
                    <Button type="submit" variant="contained" color="primary" fullWidth style={{ marginTop: "10px" }} onClick={async ()=>{
                        await addContact();
                    }}>
                        Submit
                    </Button>
                </Box>
            </Modal>
            <div style={{ "width": "100%", display: "flex", alignItems: "center", justifyContent: "center", flexDirection: "column" }}>
                <CustomButton mt="0px" color="orange" type="add" click={() => { setOpenModal(true); }} />
                <div height="20px" />
                <CustomButton mt="20px" color="green" type="phone" click={async () => {
                    try{
                        var res=await axios.post(url+"call-sequence");
                        if(res.data.is_free===true){
                            toast.success("Starting emergency sequence....",{
                                position: toast.POSITION.TOP_RIGHT,
                            });
                        }else{
                            toast.info("An emergency sequence is already running...",{
                                position: toast.POSITION.TOP_RIGHT,
                            });
                        }
                    }catch(e){
                        toast.error("An error occurred!",{
                            position: toast.POSITION.TOP_RIGHT,
                        });
                    }
                }}
                disabled={props.disabled} 
                />
            </div>
        </div>
    );
}

export default CallAddSection;