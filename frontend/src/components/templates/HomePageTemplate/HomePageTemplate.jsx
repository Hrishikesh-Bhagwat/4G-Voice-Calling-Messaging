import React from 'react';
import "./HomePageTemplate.css";
import CallSection from '../../organisms/CallSection/CallSection';
import 'react-toastify/dist/ReactToastify.css';
import TableComponent from '../../organisms/TableComponent/TableComponent';
// import Diagnostics from '../../organisms/Diagnostics/Diagnostics';

function HomePageTemplate(props) {
    return (
        <div className='main-div'>
            <div className='table-section'>
                <div style={{height:"30px"}}></div>
                {/* <Diagnostics/> */}
                <TableComponent/>
            </div>
            <div className='contact-section'>
                <CallSection disabled={props.disabled}/>
            </div>
        </div>
    );
}

export default HomePageTemplate;