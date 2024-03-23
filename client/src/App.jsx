import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import EsriData from './components/EsriData'
import { Grid } from '@mui/material'

function App() {

    return (
        <div>
            <Grid container justifyContent="center" alignItems="center">
                <Grid item xs={10}>
                    <EsriData />

                </Grid>
                
            </Grid>
        </div>
    )
}

export default App
