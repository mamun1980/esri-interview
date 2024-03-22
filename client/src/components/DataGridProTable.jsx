import { DataGrid } from '@mui/x-data-grid';
import React from 'react'


const columns = [
    { field: 'block', headerName: 'Block', width: 150 },
    { field: 'usi_code', headerName: 'USI Code', width: 350 },
    { field: 'region', headerName: 'Region', width: 150 },
    { field: 'length_km', headerName: 'Length in KM', width: 150 },
    { field: 'acquisition_year', headerName: 'Acquisition Year', width: 150 },
    { field: 'processing_year', headerName: 'Processing Year', width: 150 },
    ];
    

const DataGridProTable = () => {
    const [rows, setRows] = React.useState([]);
    const [paginationModel, setPaginationModel] = React.useState({
        page: 0,
        pageSize: 10,
    });
    const [filterModel, setFilterModel] = React.useState({ items: [] });
    const [sortModel, setSortModel] = React.useState([]);

    React.useEffect(() => {
    const fetcher = async () => {
        // fetch data from server
        const data = await fetch('http://127.0.0.1:8000/api/esri/?format=json&limit=20&offset=20', {
            method: 'GET',
            body: JSON.stringify({
                page: paginationModel.page,
                pageSize: paginationModel.pageSize,
                sortModel,
                filterModel,
            }),
        });
        setRows(data.rows);
    };
    fetcher();
    }, [paginationModel, sortModel, filterModel]);

    return (
        <DataGrid
            columns={columns}
            pagination
            sortingMode="server"
            filterMode="server"
            paginationMode="server"
            onPaginationModelChange={setPaginationModel}
            onSortModelChange={setSortModel}
            onFilterModelChange={setFilterModel}
        />
    )

}

export default DataGridProTable
