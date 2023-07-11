import axios from "axios";
import url from "../../../url";
import { Delete } from "@mui/icons-material";

function ColumnItem({text,id,column,selected,reload}){
    async function updateStatus(){
        axios.post(url + "table-entries/update-state",{id:id,col:column,status:!selected}).then(async res=>{
            await reload();
        }).catch(e=>{
            console.log(e);
        });
    }
    async function deleteItem(){
        axios.post(url + "table-entries/delete-entry",{column_id:column,entry_id:id}).then(async res=>{
            await reload();
        }).catch(e=>{
            console.log(e);
        });
    }
    return (
        <div style={{height:"30px",width:"100%",backgroundColor:selected===false?"white":"green",maxWidth:"100%",display:"flex",alignItems:"center",cursor:"pointer",justifyContent:"space-between"}} onClick={async ()=>{
            await updateStatus();
        }}>
            <span style={{fontWeight:"600",marginLeft:"5px",fontSize:"13px",color:selected===false?"black":"white"}}>{text}</span>
            <span onClick={async ()=>{
                await deleteItem();
            }}><Delete style={{color:"red",fontSize:"15"}}/></span>
        </div>
    );
}

export default ColumnItem;