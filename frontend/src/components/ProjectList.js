import UserList from "./UserList";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.repository}
            </td>
            <td>
                <UserList users = {project.users} />
            </td>
        </tr>
    )
}

const ProjectsList = ({projects}) => {
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Repository
            </th>
            <th>
                Users
            </th>
            {projects.map((project) => <ProjectItem project = {project} />)}
        </table>
    )
}

export default ProjectsList