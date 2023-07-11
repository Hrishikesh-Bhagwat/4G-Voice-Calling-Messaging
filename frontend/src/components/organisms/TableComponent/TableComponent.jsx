import AlertText from "../../molecules/AlertText/AlertText";
import Column from "../Column/Column";
import "./TableComponent.css";
import { useEffect, useState } from "react";
import makeGETRequest from "../../../http_requests/getRequest";
import url from "../../../url";

function TableComponent() {
    const [alertText, setAlertText] = useState('');
    const [column1Heading,setColumn1Heading]=useState({col:'',title:''});
    const [column2Heading,setColumn2Heading]=useState({col:'',title:''});
    const [column3Heading,setColumn3Heading]=useState({col:'',title:''});
    const [column4Heading,setColumn4Heading]=useState({col:'',title:''});
    const [column5Heading,setColumn5Heading]=useState({col:'',title:''});
    const [column6Heading,setColumn6Heading]=useState({col:'',title:''});

    const [column1Entries,setColumn1Entries]=useState([]);
    const [column2Entries,setColumn2Entries]=useState([]);
    const [column3Entries,setColumn3Entries]=useState([]);
    const [column4Entries,setColumn4Entries]=useState([]);
    const [column5Entries,setColumn5Entries]=useState([]);
    const [column6Entries,setColumn6Entries]=useState([]);

    async function fetchTable() {
        try {
            var res = await makeGETRequest(url + "table-entries");
            var data=res.data;
            setAlertText(data.text);
            setColumn1Heading({
                title: res.data.col1.heading.title,
                col: "col1"
            });
            setColumn2Heading({
                title: res.data.col2.heading.title,
                col: "col2"
            });
            setColumn3Heading({
                title: res.data.col3.heading.title,
                col: "col3"
            });
            setColumn4Heading({
                title: res.data.col4.heading.title,
                col: "col4"
            });
            setColumn5Heading({
                title: res.data.col5.heading.title,
                col: "col5"
            });
            setColumn6Heading({
                title: res.data.col6.heading.title,
                col: "col6"
            });
            setColumn1Entries([]);
            setColumn2Entries([]);
            setColumn3Entries([]);
            setColumn4Entries([]);
            setColumn5Entries([]);
            setColumn6Entries([]);
            var temp1=[];
            var temp2=[];
            var temp3=[];
            var temp4=[];
            var temp5=[];
            var temp6=[];
            for(var i=0;i<data.col1.entries.length;i++){
                temp1.push(
                    {
                        col: "col1",
                        id: data.col1.entries[i].id,
                        text: data.col1.entries[i].text,
                        selected: data.col1.entries[i].selected,
                    }
                );
            }
            for(i=0;i<data.col2.entries.length;i++){
                temp2.push(
                    {
                        col: "col2",
                        id: data.col2.entries[i].id,
                        text: data.col2.entries[i].text,
                        selected: data.col2.entries[i].selected,
                    }
                );
            }
            for(i=0;i<data.col3.entries.length;i++){
                temp3.push(
                    {
                        col: "col3",
                        id: data.col3.entries[i].id,
                        text: data.col3.entries[i].text,
                        selected: data.col3.entries[i].selected,
                    }
                );
            }
            for(i=0;i<data.col4.entries.length;i++){
                temp4.push(
                    {
                        col: "col4",
                        id: data.col4.entries[i].id,
                        text: data.col4.entries[i].text,
                        selected: data.col4.entries[i].selected,
                    }
                );
            }
            for(i=0;i<data.col5.entries.length;i++){
                temp5.push(
                    {
                        col: "col5",
                        id: data.col5.entries[i].id,
                        text: data.col5.entries[i].text,
                        selected: data.col5.entries[i].selected,
                    }
                );
            }
            for(i=0;i<data.col6.entries.length;i++){
                temp6.push(
                    {
                        col: "col6",
                        id: data.col6.entries[i].id,
                        text: data.col6.entries[i].text,
                        selected: data.col6.entries[i].selected,
                    }
                );
            }
            setColumn1Entries(temp1);
            setColumn2Entries(temp2);
            setColumn3Entries(temp3);
            setColumn4Entries(temp4);
            setColumn5Entries(temp5);
            setColumn6Entries(temp6);            
        } catch (e) {
            setAlertText('');
            setColumn1Entries([]);
            setColumn2Entries([]);
            setColumn3Entries([]);
            setColumn4Entries([]);
            setColumn5Entries([]);
            setColumn6Entries([]);
        }
    }

    useEffect(() => {
        fetchTable();
    }, []);

    return (
        <div className="table-component">
            <AlertText message={alertText}/>
            <div style={{ height: "100%", width: "100%", display: "flex" }}>
                <Column reload={fetchTable} columnHeading={column1Heading} entries={column1Entries}/>
                <Column reload={fetchTable} columnHeading={column2Heading} entries={column2Entries}/>
                <Column reload={fetchTable} columnHeading={column3Heading} entries={column3Entries}/>
                <Column reload={fetchTable} columnHeading={column4Heading} entries={column4Entries}/>
                <Column reload={fetchTable} columnHeading={column5Heading} entries={column5Entries}/>
                <Column reload={fetchTable} columnHeading={column6Heading} entries={column6Entries}/>
            </div>
        </div>
    );
}

export default TableComponent;