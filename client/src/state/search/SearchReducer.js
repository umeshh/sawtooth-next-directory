/* Copyright 2019 Contributors to Hyperledger Sawtooth

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
----------------------------------------------------------------------------- */


import { createReducer } from 'reduxsauce';
import { INITIAL_STATE, SearchTypes as Types } from './SearchActions';


export const request = {
  search: (state) => state.merge({ fetching: true }),
};


export const failure = (state, { error }) =>
  state.merge({ fetching: false, error });


export const clearSearchData = () =>
  INITIAL_STATE;


export const success = {
  browse: (state, { result }) =>
    result.page > 1 ?
      state.merge({
        fetching: false,
        packs: [...(state.packs || []), ...result.packs],
        roles: [...(state.roles || []), ...result.roles],
        totalPages: result.total_pages,
      }) :
      state.merge({
        fetching: false,
        packs: result.packs,
        roles: result.roles,
        totalPages: result.total_pages,
      }),
  people: (state, { result }) =>
    result.page > 1 ?
      state.merge({
        fetching: false,
        people: [...(state.people || []), ...result.users],
        totalPages: result.total_pages,
      }) :
      state.merge({
        fetching: false,
        people: result.users,
        totalPages: result.total_pages,
      }),
};


export const SearchReducer = createReducer(INITIAL_STATE, {
  [Types.SEARCH_BROWSE_REQUEST]:   request.search,
  [Types.SEARCH_BROWSE_SUCCESS]:   success.browse,
  [Types.SEARCH_BROWSE_FAILURE]:   failure,

  [Types.SEARCH_PEOPLE_REQUEST]:   request.search,
  [Types.SEARCH_PEOPLE_SUCCESS]:   success.people,
  [Types.SEARCH_PEOPLE_FAILURE]:   failure,

  [Types.CLEAR_SEARCH_DATA]:       clearSearchData,
});
