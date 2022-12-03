#  Copyright (c) 2003-2022 Movella Technologies B.V. or subsidiaries worldwide.
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without modification,
#  are permitted provided that the following conditions are met:
#
#  1.	Redistributions of source code must retain the above copyright notice,
#  	this list of conditions and the following disclaimer.
#
#  2.	Redistributions in binary form must reproduce the above copyright notice,
#  	this list of conditions and the following disclaimer in the documentation
#  	and/or other materials provided with the distribution.
#
#  3.	Neither the names of the copyright holders nor the names of their contributors
#  	may be used to endorse or promote products derived from this software without
#  	specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
#  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
#  THE COPYRIGHT HOLDERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
#  OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
#  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY OR
#  TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import getpass
import xsensdot_pc_sdk

measuremode_dic = {
    'Undefined': xsensdot_pc_sdk.XsPayloadMode_Undefined,
    'HighFidelitywMag': xsensdot_pc_sdk.XsPayloadMode_HighFidelitywMag,
    'ExtendedQuaternion': xsensdot_pc_sdk.XsPayloadMode_ExtendedQuaternion,
    'CompleteQuaternion': xsensdot_pc_sdk.XsPayloadMode_CompleteQuaternion,
    'OrientationEuler': xsensdot_pc_sdk.XsPayloadMode_OrientationEuler,
    'OrientationQuaternion': xsensdot_pc_sdk.XsPayloadMode_OrientationQuaternion,
    'FreeAcceleration': xsensdot_pc_sdk.XsPayloadMode_FreeAcceleration,
    'ExtendedEuler': xsensdot_pc_sdk.XsPayloadMode_ExtendedEuler,
    'CompleteEuler': xsensdot_pc_sdk.XsPayloadMode_CompleteEuler,
    'HighFidelity': xsensdot_pc_sdk.XsPayloadMode_HighFidelity,
    'DeltaQuantitieswMag': xsensdot_pc_sdk.XsPayloadMode_DeltaQuantitieswMag,
    'DeltaQuantities': xsensdot_pc_sdk.XsPayloadMode_DeltaQuantities,
    'RateQuantitieswMag': xsensdot_pc_sdk.XsPayloadMode_RateQuantitieswMag,
    'RateQuantities': xsensdot_pc_sdk.XsPayloadMode_RateQuantities,
    'CustomMode1': xsensdot_pc_sdk.XsPayloadMode_CustomMode1,
    'CustomMode2': xsensdot_pc_sdk.XsPayloadMode_CustomMode2,
    'CustomMode3': xsensdot_pc_sdk.XsPayloadMode_CustomMode3,
    'CustomMode4': xsensdot_pc_sdk.XsPayloadMode_CustomMode4,
    'CustomMode5': xsensdot_pc_sdk.XsPayloadMode_CustomMode5, }
whitelist = list()
dot_basename = "xsens"
username = getpass.getuser().lower()
whitelist = {}
dot_basename = "Xsens DOT"
