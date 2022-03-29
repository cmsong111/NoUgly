package com.gdsc.nougly

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

data class LoginOutput (
    var user: UserInfo,
    var token: String,
    @SerializedName("non_field_errors")
    @Expose
    var nonfielderrors: String
)

data class UserInfo (
    var id: String,
    var email: String,
    var name: String,
    var date: String,
    var gender: String,
    var address: String,
    @SerializedName("phone_num")
    @Expose
    var phoneNum: String
)

