import { MoreHoriz } from "@mui/icons-material";
import { Typography, Popover, Modal, Box, TextField, Button} from "@mui/material";
import { useState } from "react";
import React from "react";
import url from "../../../url";

function Heading({ column, text, reload }) {
    const [anchorEl, setAnchorEl] = React.useState(null);

    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    async function addEntry(){
        if(addEntryText.trim().length===0){
            setAddEntryError('Please give appropriate text');
            return;
        }
        if(addEntryFile===null){
            setAddEntryError('Please select audio file');
            return;
        }
        console.log(addEntryFile);

        const formData= new FormData();
        formData.append(
            "text",addEntryText,
        );
        formData.append(
            "col",column
        );
        formData.append(
            "file",addEntryFile
        );

        fetch(url+"table-entries/add-entry", {
            method: "POST",
            body: formData,
        }).then((res) =>{
            if(res.status===200){
                reload();
                setAddEntryText('');
                setAddEntryFile(null);
                setAddEntryError('');
                setOpenAddEntryModal(false);
            }
        }).catch(e=>{
            setAddEntryError('Some error occurred!')
        });
    }

    async function modifyHeading(){
        if(heading.trim().length===0){
            setError('Please give appropriate heading');
            return;
        }
        if(file===null){
            setError('Please select audio file');
            return;
        }
        console.log(file);
        const formData= new FormData();
        formData.append(
            "text",heading,
        );
        formData.append(
            "col",column
        );
        formData.append(
            "file",file
        );

        fetch(url+"table-entries/update-heading", {
            method: "POST",
            body: formData,
        }).then((res) =>{
            if(res.status===200){
                reload();
                setHeading('');
                setFile(null);
                setError('');
                setOpenModal(false);
            }
        }).catch(e=>{
            setError('Some error occurred!')
        });
    }

    const [openAddEntryModal,setOpenAddEntryModal]=useState(false);
    const [addEntryText,setAddEntryText]=useState('');
    const [addEntryFile,setAddEntryFile]=useState(null);
    const [addEntryError,setAddEntryError]=useState('');

    const open = Boolean(anchorEl);
    const [openModal,setOpenModal]=useState(false);
    const [heading,setHeading]=useState('');
    const [file,setFile]=useState(null);
    const [error,setError]=useState('');
    const id = open ? 'simple-popover' : undefined;
    return (
        <div style={{width:"100%"}}>
            <Modal open={openModal} onClose={() => {
                setOpenModal(false);
                setHeading('');
                setFile('');
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
                        boxShadow: 24,
                        p: 2,
                        border:"none",
                        outline:"none"
                    }}
                >
                    <div>
                        <b style={{ fontSize: "18px" }}>New heading for {text}</b>
                    </div>
                    <TextField
                        label="Heading"
                        variant="outlined"
                        fullWidth
                        margin="normal"
                        value={heading}
                        onChange={e => setHeading(e.target.value)}
                    />
                    <Button variant="outlined" color="primary" fullWidth style={{ marginTop: "10px" }} component="label">
                        {file===null?"Select File":"Modify File Selection"}
                    <input
                        type="file"
                        hidden
                        accept=".mp3"
                        onChange={(e)=>setFile(e.target.files[0])}
                    />
                    </Button>
                    
                    <div style={{ width: "100%", display: "flex", justifyContent: "center", marginTop: "3px", marginBottom: "3px",color:"red"}}>
                        {error}
                    </div>
                    <Button type="submit" variant="contained" color="primary" fullWidth style={{ marginTop: "10px" }} onClick={async ()=>{
                        await modifyHeading();
                    }}>
                        Submit
                    </Button>
                </Box>
            </Modal>
            <Modal open={openAddEntryModal} onClose={() => {
                setOpenAddEntryModal(false);
                setAddEntryText('');
                setAddEntryFile('');
                setAddEntryError('');
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
                        boxShadow: 24,
                        p: 2,
                        outline:"none"
                    }}
                >
                    <div>
                        <b style={{ fontSize: "18px" }}>New entry in {text}</b>
                    </div>
                    <TextField
                        label="New entry name"
                        variant="outlined"
                        fullWidth
                        margin="normal"
                        value={addEntryText}
                        onChange={e => setAddEntryText(e.target.value)}
                    />
                    <Button variant="outlined" color="primary" fullWidth style={{ marginTop: "10px" }} component="label">
                        {addEntryFile===null?"Select File":"Modify File Selection"}
                    <input
                        type="file"
                        hidden
                        accept=".mp3"
                        onChange={(e)=>setAddEntryFile(e.target.files[0])}
                    />
                    </Button>
                    
                    <div style={{ width: "100%", display: "flex", justifyContent: "center", marginTop: "3px", marginBottom: "3px",color:"red"}}>
                        {addEntryError}
                    </div>
                    <Button type="submit" variant="contained" color="primary" fullWidth style={{ marginTop: "10px" }} onClick={async ()=>{
                        await addEntry();
                    }}>
                        Submit
                    </Button>
                </Box>
            </Modal>
            <div style={{ height: "20px", width: "100%", display: "flex", backgroundColor: "white", justifyContent: "space-between", paddingBottom: "3px",marginBottom:"20px"}}>
                <b style={{ marginRight: "5px",fontSize:"14px"}}>{text}</b>
                <div>
                    <div onClick={handleClick}>
                        <MoreHoriz style={{ color: "grey", marginRight: "5px", cursor: "pointer" }} id={column} />
                    </div>
                    <Popover id={id}
                        open={open}
                        anchorEl={anchorEl}
                        onClose={handleClose}
                        anchorOrigin={{
                            vertical: 'bottom',
                            horizontal: 'left',
                        }}
                        style={{
                            height: "300px",
                        }}
                    >
                        <Typography sx={{ p: 2,display:"block",cursor:"pointer"}} component="span" onClick={() => {
                            setOpenModal(true);
                            setAnchorEl(null);
                        }}>Modify column heading</Typography>
                        <Typography sx={{ p: 2,display:"block",cursor:"pointer"}} component="span" onClick={() => {
                            setOpenAddEntryModal(true);
                            setAnchorEl(null);
                        }}>Add new entry</Typography>
                    </Popover>
                </div>
            </div>
        </div>
    );
}

export default Heading;