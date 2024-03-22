import { Autocomplete, Container, Grid, Paper, TextField } from '@mui/material'
import './App.css'
import ButtonAppBar from './components/Navbar'
import DataTable from './components/DataTable'

function App() {

    return (
        <>
            <Grid container spacing={2} justifyContent="center" alignItems="center">
                <Grid item xs={8}>
                    <Paper elevation={3} className=''>
                        
                    <TextField  label="Search" variant="standard" fullWidth  />
                    </Paper>
                </Grid>

                <Grid item xs={8}>
                    <DataTable />
                </Grid>
                
            </Grid>
        </>
    )
}

export default App
