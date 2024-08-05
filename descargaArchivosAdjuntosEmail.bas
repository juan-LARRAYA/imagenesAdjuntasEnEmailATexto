Attribute VB_Name = "Módulo11"
Sub DescargarAdjuntosDeCorreosNoLeidos()
    Dim OutlookApp As Outlook.Application
    Dim OutlookNamespace As Outlook.Namespace
    Dim CarpetaBandejaEntrada As Outlook.MAPIFolder
    Dim CarpetaAutomatizacion As Outlook.MAPIFolder
    Dim CarpetaSistema As Outlook.MAPIFolder
    Dim CarpetaRecepcionComponentes As Outlook.MAPIFolder
    Dim Elementos As Outlook.Items
    Dim Elemento As Object
    Dim Adjunto As Outlook.Attachment
    Dim FileSystem As Object
    Dim RutaArchivo As String
    Dim CarpetaDestino As String
    
    ' Inicializar aplicación de Outlook
    On Error Resume Next
    Set OutlookApp = New Outlook.Application
    Set OutlookNamespace = OutlookApp.GetNamespace("MAPI")
    On Error GoTo 0
    
    If OutlookApp Is Nothing Or OutlookNamespace Is Nothing Then
        MsgBox "Error al inicializar Outlook. Asegúrese de que Outlook esté instalado y configurado correctamente.", vbCritical
        Exit Sub
    End If
    
    ' Obtener la carpeta Bandeja de entrada
    On Error Resume Next
    Set CarpetaBandejaEntrada = OutlookNamespace.Folders("TUMAIL@ALGO.com").Folders("Bandeja de entrada")
    On Error GoTo 0
    
    If CarpetaBandejaEntrada Is Nothing Then
        MsgBox "No se encontró la carpeta 'Bandeja de entrada'. Verifica el nombre y la jerarquía de carpetas.", vbCritical
        Exit Sub
    End If
    
    ' Obtener la carpeta Automatizacion dentro de Bandeja de entrada
    On Error Resume Next
    Set CarpetaAutomatizacion = CarpetaBandejaEntrada.Folders("Automatizacion")
    On Error GoTo 0
    
    If CarpetaAutomatizacion Is Nothing Then
        MsgBox "No se encontró la carpeta 'Automatizacion'. Verifica el nombre y la jerarquía de carpetas.", vbCritical
        Exit Sub
    End If
    
    ' Obtener la carpeta Sistema dentro de Automatizacion
    On Error Resume Next
    Set CarpetaSistema = CarpetaAutomatizacion.Folders("Sistema")
    On Error GoTo 0
    
    If CarpetaSistema Is Nothing Then
        MsgBox "No se encontró la carpeta 'Sistema'. Verifica el nombre y la jerarquía de carpetas.", vbCritical
        Exit Sub
    End If
    
    ' Obtener la carpeta Recepcion de componentes dentro de Sistema
    On Error Resume Next
    Set CarpetaRecepcionComponentes = CarpetaSistema.Folders("Recepcion de componentes")
    On Error GoTo 0
    
    If CarpetaRecepcionComponentes Is Nothing Then
        MsgBox "No se encontró la carpeta 'Recepcion de componentes'. Verifica el nombre y la jerarquía de carpetas.", vbCritical
        Exit Sub
    End If
    
    ' Obtener los elementos de la carpeta Recepcion de componentes
    Set Elementos = CarpetaRecepcionComponentes.Items

    ' Inicializar el objeto de sistema de archivos
    Set FileSystem = CreateObject("Scripting.FileSystemObject")
    
    ' Carpeta de destino para guardar los archivos adjuntos
    CarpetaDestino = "C:\Users\juan.larraya\Downloads\fotosOutlook\a"
    
    ' Recorrer los correos no leídos y descargar los adjuntos
    For Each Elemento In Elementos
        If Elemento.Class = olMail And Elemento.UnRead = True Then
            For Each Adjunto In Elemento.Attachments
                RutaArchivo = CarpetaDestino & Adjunto.Filename
                Adjunto.SaveAsFile RutaArchivo
            Next Adjunto
            ' Marcar el correo como leído
            Elemento.UnRead = True
            Elemento.Save
        End If
    Next Elemento
    
    
    ' Liberar objetos
    Set Adjunto = Nothing
    Set Elemento = Nothing
    Set Elementos = Nothing
    Set CarpetaRecepcionComponentes = Nothing
    Set CarpetaSistema = Nothing
    Set CarpetaAutomatizacion = Nothing
    Set CarpetaBandejaEntrada = Nothing
    Set OutlookNamespace = Nothing
    Set OutlookApp = Nothing
    Set FileSystem = Nothing
    
    MsgBox "Archivos adjuntos descargados correctamente."
End Sub

