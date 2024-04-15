import Navbar from './navbar'
import AllSheet from './pages/osszesmunkalap'
import InactiveSheet from './pages/lezartmunkalap'
import ActiveSheet from './pages/aktivmunkalap'
import NewSheet from './pages/ujmunkalap'
import ViewSheet from './pages/viewsheet'
import Welcome from './pages/welcome'

const App = () => {
  let component
  switch (window.location.pathname) {
    case "/":
      component = <Welcome />
      break;
    case "/viewsheet":
      component = <ViewSheet />
      break;
    case "/ujmunkalap":
      component = <NewSheet />
      break;
    case "/aktivmunkalap":
      component = <ActiveSheet />
      break;
    case "/lezartmunkalap":
      component = <InactiveSheet />
      break;
    case "/osszesmunkalap":
      component = <AllSheet />
      break;
    default:
      break;
  }


  return (
    <>
      <Navbar />
      <div className="component">{component}</div>
    </>
  )
}

export default App

