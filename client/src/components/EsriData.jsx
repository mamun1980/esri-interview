import React, { useEffect, useState } from 'react'
import { FaSearch } from "react-icons/fa";
import { DataGrid } from '@mui/x-data-grid';
import { Box } from '@mui/material';
import axios from 'axios';


const columns = [
    { field: 'block', headerName: 'Block', width: 200 },
    { field: 'usi_code', headerName: 'USI Code', width: 300 },
    { field: 'region', headerName: 'Region', width: 150 },
    { field: 'length_km', headerName: 'Length in KM', width: 150 },
    { field: 'acquisition_year', headerName: 'Acquisition Year', width: 150 },
    { field: 'processing_year', headerName: 'Processing Year', width: 150 },
];


const EsriData = () => {
    const [input, setInput] = useState("");
    const handleChange = (value) => {
        setInput(value);
           
    };

    const handleSubmit = (e) => {
        e.preventDefault()
        const newurl = url + `&q=${input}`
        setUrl(newurl)
        setInput("")

    }

    const [paginationModel, setPaginationModel] = useState({
        page: 0,
        pageSize: 10,
    });
    const [data, setData] = useState({
        loading: true,
        rows: [],
        totalRows: 0,
        pageSize: paginationModel.pageSize,
        page: paginationModel.page
    })
    const [url, setUrl] = useState("https://charlicoder.com/api/esri/?format=json")

    const updateData = (k, v) => setData((prev) => ({ ...prev, [k]: v }));

    useEffect(() => {
        axios.get(url)
        .then(res => {
            console.log(res.data);
            setTimeout(() => {
                updateData("totalRows", res.data.count);
                updateData("rows", res.data.results);
                updateData("loading", false);
            }, 200)
        })
        .catch(err => console.log(err))
    }, [data.page, url])
    
    return (
        <div>
            <div className="input-wrapper">
                <form onSubmit={handleSubmit}>
                <input type="search" placeholder="Type to search..." value={input} onChange={(e) => handleChange(e.target.value)} />
                    <button type="submit">Search</button>
                </form>
            </div>
            <br />
            <Box sx={{ height: 650, width: '100%' }}>
                <DataGrid
                    rows={data.rows}
                    columns={columns}
                    initialState={{
                        pagination: {
                            paginationModel: {
                            pageSize: 10,
                            },
                        },
                    }}
                    pageSizeOptions={[10]}
                    disableRowSelectionOnClick
                />
            </Box>
        </div>
    )
}

export default EsriData
