import React, { useState } from "react";
import TextField from "@material-ui/core/TextField";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";
import { Button } from "@material-ui/core";
import { styles } from "./styles";
import InputMask from "react-input-mask";
import axios from "axios";

const App = () => {
  const classes = styles();
  const [fornecedor, setFornecedor] = useState("");
  const [dataVencimento, setDataVencimento] = useState("");
  const [pago, setPago] = useState("");
  const [notaFiscal, setNotaFiscal] = useState("");

  const refreshList = () => {};

  const handleSubmit = () => {
    let item = {
      fornecedor: fornecedor,
      dataVencimento: dataVencimento,
      pago: pago,
      notaFiscal: notaFiscal,
    };
    axios
      .post("http://localhost:8000/api/crud/", item)
      .then((res) => refreshList());
  };
  return (
    <div className={classes.container}>
      <h2>Cadastro de contas a pagar</h2>


      <Select
        className={classes.select}
        onChange={({ target }) => setFornecedor(target.value)}
        value={fornecedor}
        label="Fornecedor"
      >
        <MenuItem value={"for_1"}>Fornecedor 1</MenuItem>
        <MenuItem value={"for_2"}>Fornecedor 2</MenuItem>
      </Select>

      <InputMask
        className={classes.select}
        mask="99/99/9999"
        onChange={({ target }) => setDataVencimento(target.value)}
        value={dataVencimento}
        label="Data de vencimento"
      />

      <Select
        className={classes.select}
        onChange={({ target }) => setPago(target.value)}
        value={pago}
        label="Pago"
      >
        <MenuItem value={"sim"}>Sim</MenuItem>
        <MenuItem value={"nao"}>Nao</MenuItem>
      </Select>

      <TextField
        onChange={({ target }) => setNotaFiscal(target.value)}
        value={notaFiscal}
        label={"IDs de nota fiscal"}
      />

      <div>
        <Button onClick={handleSubmit}>Submit</Button>
      </div>
    </div>
  );
};

export default App;
