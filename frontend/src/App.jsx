import HousePricePredictor from "./components/HousePricePredictor"

function App() {

  return (
    <div className="price-pred">
      <header className='price-pred-header'>
        <h1>House Price Prediction App</h1>
      </header>

      <main>
        <HousePricePredictor/>
      </main>
    </div>
  )
}; 

export default App
