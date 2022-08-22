const NoteItem = ({note}) => {
    return (
        <tr>
            <td>
                {note.project}
            </td>
            <td>
                {note.text}
            </td>
            <td>
                {note.user}
            </td>
            <td>
                {note.active}
            </td>
        </tr>
    )
}

const NoteList = ({notes}) => {
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Text
            </th>
            <th>
                User
            </th>
            <th>
                Active
            </th>
            {notes.map((note) => <NoteItem note= {note} />)}
        </table>
    )
}

export default NoteList