import { Route, Routes } from 'react-router';
import { Provider } from 'react-redux';
import MainPage from './pages/MainPage';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';
import UserPage from './pages/UserPage';
import UserEditPage from './pages/UserEditPage';
import store from './store';

function App() {
  return (
    <Provider store={store}>
      <Routes>
        <Route index element={<MainPage />}></Route>
        <Route path='register' element={<RegisterPage />}></Route>
        <Route path='login' element={<LoginPage />}></Route>
        <Route path='user' element={<UserPage />}></Route>
        <Route path='user/edit' element={<UserEditPage />}></Route>
      </Routes>
    </Provider>
  );
}

export default App;