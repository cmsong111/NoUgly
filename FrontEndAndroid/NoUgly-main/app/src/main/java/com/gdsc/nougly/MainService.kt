package com.gdsc.nougly

import retrofit2.Call
import retrofit2.http.GET

interface MainService {
    @GET("store/products/random")

    fun requestMain(): Call<ArrayList<MainOutput>>
}