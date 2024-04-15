import React, { useEffect, useState } from 'react'


const AllSheet = () => {
  const [apiData, setApiData] = useState()

  useEffect(()=>{
    fetch('http://localhost:8000/allsheet.json')
    .then(res => res.json())
    .then(data => setApiData(data))
  }, [])

  return (
    <div id="allsheet">
        <h2>Összes munkalap</h2>
        <div className="cards">
            {
            apiData ?
            apiData.map((data, idx) => <AllSheetCard key={idx} {...data} />) :
            <div>Adatok betöltése...</div>
            }
        </div>
    </div>
  )
}
export default AllSheet

const AllSheetCard = (props) => {

    const viewButton = () => {
        console.log("kattintottam")
    }

  return (
    <div className='card'>
        <table>
            <tbody>
                <tr>
                    <th>Munkalapszám:</th>
                    <th>{props.munkalapszam}</th>
                </tr>
                <tr>
                    <td>Név:</td>
                    <td>{props.megrendelo_neve}</td>
                </tr>
                <tr>
                    <td>Státusz:</td>
                    <td className={props.munkalapstatusz === 'Aktív' ? "astatusz" : "lstatusz"}>{props.munkalapstatusz}</td>
                </tr>
                <tr>
                    <td>Üzemanyagszint:</td>
                    <td>{props.uzemanyagszint}</td>
                </tr>
                <tr>
                    <td>Hiba:</td>
                    <td>{props.hiba}</td>
                </tr>
                <tr>
                    <td>Márka:</td>
                    <td>{props.gepjarmu}</td>
                </tr>
            </tbody>
        </table>
        <button onClick={viewButton}>Megtekintés</button>
    </div>
  )
}



