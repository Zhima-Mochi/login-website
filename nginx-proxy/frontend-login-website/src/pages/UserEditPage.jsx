import Header from "../components/Header";
import UserInfoEdit from "../components/UserInfoEdit";

export default function UserEditPage(){
    return (
        <div className="flex flex-col min-h-screen bg-blue-50">
            <Header showStatus={true} />
            <div className="flex flex-col my-16">
                <h1 className="text-center text-2xl text-blue-800 font-medium">Edit User Information</h1>
                <div className="mx-auto my-8">
                    <UserInfoEdit />
                </div>
            </div>
        </div >
    );
}