import React from 'react';

import { createAsyncThunk } from '@reduxjs/toolkit';

/* eslint-disable-next-line */
export interface SharedAccountSynApiProps {}

export type SignInError = any;

export interface SignUpState {
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  password: string;
}

export interface SignInState {
  login: {
    email: string;
    password: string;
  };
  token: string;
  authorised: boolean;
  error: SignInError;
}

const API_URL = 'http://localhost:5000/';

export function SharedAccountSynApi(props: SharedAccountSynApiProps) {
  return;
}

export const postSignUpUser = createAsyncThunk(
  'malliva/register',
  async (payload: SignUpState) => {
    const response = await fetch(
      API_URL + 'api/v1/user/register' + JSON.stringify(payload)
    );
    if (response.ok) {
      const serverResponse = response.json();
      return { serverResponse };
    }
    return response.json();
  }
);

export const getSingInUser = createAsyncThunk(
  'malliva/login',
  async (payload: SignInState) => {
    const response = await fetch(
      API_URL + 'api/v1/user/login' + JSON.stringify(payload.login)
    );
    if (response.ok) {
      const serverResponse = response.json();
      return { serverResponse };
    }
    return response.json();
  }
);
