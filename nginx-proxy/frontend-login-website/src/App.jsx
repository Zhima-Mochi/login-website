import { Route, Routes } from 'react-router';
import { Provider } from 'react-redux';
import MainPage from './pages/MainPage';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';

function App() {
  return (
    // <Provider store={null}>
      <Routes>
        <Route path='/' element={<MainPage />}></Route>
        <Route path='/register' element={<RegisterPage />}></Route>
        <Route path='/login' element={<LoginPage />}></Route>
      </Routes>
    // </Provider>
  );
}

export default App;