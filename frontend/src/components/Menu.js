import {Link} from "react-router-dom";

const MenuItem = ({link}) =>{
    return (
        <li>
            <Link to={link.href}>{link.name}</Link>
        </li>
    )
}

const Menu =({menu})=> {
    return (<>
            {menu.map((link) => <MenuItem link = {link} />)}
            </>
    )
}

export default Menu