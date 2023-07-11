import React from 'react';
import Modal from '@mui/material/Modal';
import Box from '@mui/material/Box';
import CircularProgress from '@mui/material/CircularProgress';
import Typography from '@mui/material/Typography';
import { Dangerous, Done } from '@mui/icons-material';

const styles = {
  modal: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    // Center the modal horizontally
    marginLeft: 'auto',
    marginRight: 'auto',
    outline:'none',
    border:'none'
  },
  modalContent: {
    backgroundColor: '#fff',
    padding: '16px',
    textAlign: 'center',
    outline:'none'
  },
};

function LoadingModal({isOpen,message}) {
  return (
    <Modal open={isOpen} style={styles.modal}>
      <Box style={styles.modalContent}>
        {/* {message.type==="waiting"?<CircularProgress color="primary" size={48} />:<Dangerous si/>} */
            // <Dangerous style={{color:"red",fontSize:"23px"}}/>
            //<Done style={{color:"green",fontSize:"23px"}}/>
            message.type==="waiting"?<CircularProgress color="primary" size={48} />:(
                message.type==="done"?<Done style={{color:"green",fontSize:"23px"}}/>:<Dangerous style={{color:"red",fontSize:"23px"}}/>
            )
        }
        <Typography variant="body1" color="textSecondary" align="center" fontWeight={"600"}>
          {message.message}
        </Typography>
      </Box>
    </Modal>
  );
}

export default LoadingModal;