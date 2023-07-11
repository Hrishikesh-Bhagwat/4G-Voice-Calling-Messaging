import ColumnItem from "../../molecules/ColumnItem/ColumnItem";
import Heading from "../../molecules/Heading/Heading";

function Column({columnHeading,reload,entries}) {
    return (
        <div style={{ width: "16.6%", height: "350px"}}>
            <Heading text={columnHeading.title} column={columnHeading.col} reload={reload}/>
            <div style={{width:"100%",height:"330px",overflowY:"scroll"}}>
                {
                    entries.map(e=><ColumnItem text={e.text} selected={e.selected} id={e.id} column={e.col} reload={reload} key={e.id}/>)
                }
            </div>
        </div>
    );
}

export default Column;