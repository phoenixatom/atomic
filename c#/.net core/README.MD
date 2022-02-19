# Useful Notes

### To copy over wwwroot contents when publishing

```
   <ItemGroup>
    <None Include="wwwroot\**">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </None>
  </ItemGroup>
  ```