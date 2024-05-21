import useForm from "./UseForm";
import getConfig from "./Data" //getConfig me retorna el ENDPOINT
import React, { useState } from "react";
import Select from "react-select";

const Form = () => {
    const { handleSubmit, status, message } = useForm();
    const {FORM_ENDPOINT} = getConfig();

    if (status === "success") {
        return (
            <>              
                <div class="tipo_mensaje">{message}</div>
                <div className="feedback">Gracias por utilizar el software</div>               
            </>
        );
    }

    if (status === "error") {
        return (
            <>
                <div class="tipo_mensaje">{message}</div>
                <div className="feedback">Hubo un error en la ejecuci&oacute;n</div>
            </>
        );
    }

    return (
        <form
            action={FORM_ENDPOINT}
            onSubmit={handleSubmit}
            method="GET"
        >   <div className="pt-0 mb-3">
                <h1 class="title">Medidor de toxicidad de un mensaje</h1>
            </div>
            <div className="pt-0 mb-3"> 
                <input
                    type="text"
                    placeholder="Mensaje"
                    name="mensaje"
                    className="focus:outline-none focus:ring relative w-full px-3 py-3 text-sm text-gray-600 placeholder-gray-400 bg-white border-0 rounded shadow outline-none"
                    required
                />
            </div>
            {status !== "loading" && (
                <div className="pt-0 mb-3">
                    <button
                        class="custom-button"
                        type="submit"
                    >
                        Calcular
                    </button>
                </div>
            )}
        </form>
    );
};

export default Form;