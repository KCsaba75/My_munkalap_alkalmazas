import React, { useEffect, useState } from 'react'

const InactiveSheet = () => {
  const [apiData, setApiData] = useState()

  useEffect(()=>{
    fetch('http://localhost:8000/inactivesheet.json')
    .then(res => res.json())
    .then(data => setApiData(data))
  }, [])

  return (
    <div id="inactivesheet">
        <h2>Lezárt munkalapok</h2>
        <div className="cards">
            {
            apiData ?
            apiData.map((data, idx) => <InactiveSheetCard key={idx} {...data} />) :
            <div>Adatok betöltése...</div>
            }
        </div>
    </div>
  )
}
export default InactiveSheet

const InactiveSheetCard = (props) => {
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
                    <td className='lstatusz'>{props.munkalapstatusz}</td>
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
      <button><a href='/viewsheet'>Megtekintés</a></button>
    </div>
  )
}

