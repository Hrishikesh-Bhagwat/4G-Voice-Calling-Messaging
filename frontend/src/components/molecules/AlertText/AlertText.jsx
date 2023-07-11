import "./AlertText.css";

function AlertText({ message }) {
    return (
        <div className="alert-text">
            <div style={{ display: "flex", width: "100%", alignItems: "center", justifyContent: "center" }}>
                <b>GENERATED MESSAGE</b>
            </div>
            <div style={{ paddingRight: "10px", paddingLeft: "10px", paddingTop: "3px", paddingBottom: "3px", maxLines: "3", overflowY: "hidden", }}>
                {message}
            </div>
        </div>
    );
}

export default AlertText;