import { DataGrid } from '@mui/x-data-grid';
import axios from 'axios';
import { useEffect, useState } from 'react';
  
const columns = [
    { field: 'block', headerName: 'Block', width: 150 },
    { field: 'usi_code', headerName: 'USI Code', width: 350 },
    { field: 'region', headerName: 'Region', width: 150 },
    { field: 'length_km', headerName: 'Length in KM', width: 150 },
    { field: 'acquisition_year', headerName: 'Acquisition Year', width: 150 },
    { field: 'processing_year', headerName: 'Processing Year', width: 150 },
];

export default function DataTable() {
    const [paginationModel, setPaginationModel] = useState({
        page: 0,
        pageSize: 10,
    });
    const [data, setData] = useState({
        loading: true,
        rows: [],
        totalRows: 0,
        rowsPerPageOptions: [5, 10, 15],
        pageSize: paginationModel.pageSize,
        page: paginationModel.page
    });

    const updateData = (k, v) => setData((prev) => ({ ...prev, [k]: v }));


    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/esri/?format=json&limit=${data.pageSize}&offset=${data.page * data.pageSize}`)
        .then(res => {
            const data = res.data.results
            console.log(data);
            updateData("totalRows", res.data.count);
            updateData("rows", res.data.results);
            updateData("loading", false);

        })
        .catch(err => console.log(err))
    }, [data.page, data.pageSize])

    
    
    return (
        <div style={{ height: 600, width: "100%" }}>
            <DataGrid 
                rows={data.rows} 
                columns={columns} 
                
                // pageSizeOptions={[5, 10, 30, 50, 100]}
                paginationMode="server"
                loading={data.loading}
                rowCount={data.totalRows}
                rowsPerPageOptions={data.rowsPerPageOptions}
                page={data.page - 1}
                pageSize={data.pageSize}
                onPaginationModelChange={(e) => {
                    console.log(e);
                    setData({...data, pageSize: e.pageSize, page: e.page})
                }}  
                onPageChange={(data) => {
                    console.log(data);
                    updateData("page", data.page + 1);
                }}
                // onPageSizeChange={(data) => {
                //     console.log(data);
                //     // updateData("page", 1);
                //     // updateData("pageSize", data.pageSize);
                // }}
            />
        </div>
    );
}