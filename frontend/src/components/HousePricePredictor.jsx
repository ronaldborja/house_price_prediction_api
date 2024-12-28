import React, { useState } from 'react';

// 1. Creación del componente 
const HousePricePredictor = () => {

  // 2. Almacenar el estado del componente 
  const [formData, setFormData] = useState({
    squareFootage: '',
    bedrooms: '',
    bathrooms: '',
    yearBuilt: '',
    lotSize: '',
    garageSize: '',
    neighborhoodQuality: ''
  });

  //3. Valor a predecir 
  const [predictedPrice, setPredictedPrice] = useState(null);
  const [error, setError] = useState('');

 // 4. Cambios en los campos el form 
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  // 5. Lógica al presionar el btn Submit 
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    // 5.1 Uso de fetch para hacer peticiones sobre la API 
    try {

      // 5.2 Forma de la petición HTPP 
      const response = await fetch('http://localhost:8000/houses/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json'},

        // Objeto js -> JSON 
        body: JSON.stringify({
          square_footage: parseFloat(formData.squareFootage),
          num_bedrooms: parseInt(formData.bedrooms),
          num_bathrooms: parseInt(formData.bathrooms),
          year_built: parseInt(formData.yearBuilt),
          lot_size: parseFloat(formData.lotSize),
          garage_size: parseInt(formData.garageSize),
          neighborhood_quality: parseInt(formData.neighborhoodQuality)
        })
      });

      // Si hay errores en la request 
      if (!response.ok) throw new Error('Failed to predict price');

      // Datos de la respuesta de la API 
      const data = await response.json();
      setPredictedPrice(data.predicted_price); //Asignar el resultado del modelo de ML 
    } catch (err) {
      setError('Error predicting price. Please try again.');
      console.error('Error:', err);
    }
  };

  // Campos del formulario: 
  const fields = [
    { name: 'squareFootage', label: 'Square Footage', type: 'number' },
    { name: 'bedrooms', label: 'Bedrooms', type: 'number' },
    { name: 'bathrooms', label: 'Bathrooms', type: 'number' },
    { name: 'yearBuilt', label: 'Year Built', type: 'number' },
    { name: 'lotSize', label: 'Lot Size', type: 'number' },
    { name: 'garageSize', label: 'Garage Size', type: 'number' },
    { name: 'neighborhoodQuality', label: 'Neighborhood Quality (1-10)', type: 'number' }
  ];

  // Renderización de la página a mostrar en el app.jsx 

  return (
    <div>      
      <form onSubmit={handleSubmit}>

        {fields.map(field => (
          <div key={field.name}>
            <label htmlFor={field.name}>{field.label}</label>
            <input
              id={field.name}
              name={field.name}
              type={field.type}
              value={formData[field.name]}
              onChange={handleChange}
              min="0"
            />
          </div>
        ))}
        
        <button type="submit">Predict Price</button>
      </form>

      {error && <p>{error}</p>}
      
      {predictedPrice && !error && (
        <div>
          <p>Predicted Price: ${predictedPrice.toLocaleString()}</p>
        </div>
      )}
    </div>
  );
};

export default HousePricePredictor;