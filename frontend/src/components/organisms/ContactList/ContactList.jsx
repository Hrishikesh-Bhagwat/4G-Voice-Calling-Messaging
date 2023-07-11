import "./ContactList.css";
import ContactItem from "../../molecules/ContactItem/ContactItem";


function ContactList({ contactList, reload }) {

    return (
        <div className="contact-list">
            {
                contactList.map(e => <ContactItem id={e.id} name={e.name} phone={e.phone} isSelected={e.isSelected} key={e.id} reload={reload} />)
            }
        </div>
    );
}

export default ContactList;