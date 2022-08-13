const MenuItem = ({link}) =>{
    return (
        <li>
            <a href={link.href}>{link.name}</a>
        </li>
    )
}

const Menu =({menu})=> {
    return (
        <ul>
            {menu.map((link) => <MenuItem link = {link} />)}
        </ul>
    )
}

export default Menu